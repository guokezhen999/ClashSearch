import pymysql

from Accounts.ClashDatabase import ClashDatabase

def get_table_names(cursor, db_name, prefix):
    query = """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = %s
                AND table_name LIKE %s; 
            """
    cursor.execute(query, (db_name, f'{prefix}\_%'))
    return [row[0] for row in cursor.fetchall()]

def get_table_columns(cursor, db_name, table_name):
    query = """
        SELECT column_name, data_type, is_nullable, column_default, extra
        FROM information_schema.columns
        WHERE table_schema = %s
        AND table_name = %s;
    """
    cursor.execute(query, (db_name, table_name))
    return {row[0]: {'data_type': row[1], 'is_nullable': row[2], 'column_default': row[3], 'extra': row[4]}
            for row in cursor.fetchall()}

def add_missing_columns(cursor, db_name, target_table, reference_columns):
    target_columns = get_table_columns(cursor, db_name, target_table)
    print(f"正在检查表: {target_table}")

    columns_to_add = {}
    for ref_col_name, ref_col_info in reference_columns.items():
        if ref_col_name not in target_columns:
            columns_to_add[ref_col_name] = ref_col_info

    if not columns_to_add:
        print(f"表 {target_table} 没有缺失的列。")
        return
    print(f"将在表 {target_table} 中添加以下缺失的列: {list(columns_to_add.keys())}")
    for col_name, col_info in columns_to_add.items():
        data_type = col_info['data_type']
        is_nullable = col_info['is_nullable']
        column_default = col_info['column_default']
        extra = col_info['extra']  # 用于处理 AUTO_INCREMENT 等属性
        # 构建 ALTER TABLE ADD COLUMN 语句
        alter_sql = f"ALTER TABLE `{target_table}` ADD COLUMN `{col_name}` {data_type}"
        # 添加 NULL / NOT NULL 约束
        if is_nullable == 'NO':
            alter_sql += " NOT NULL"
            # 如果是 NOT NULL 且没有默认值，或者默认值是 NULL (但列又不是 NULLable)，需要特别处理
            # 为了安全，如果 NOT NULL 且没有明确的非 NULL 默认值，我们尝试添加一个合适的默认值
            if column_default is None and 'auto_increment' not in extra.lower():
                # 根据数据类型设置一个默认值，这需要根据实际情况调整
                if 'int' in data_type.lower() or 'decimal' in data_type.lower() or 'double' in data_type.lower():
                    alter_sql += " DEFAULT 0"
                elif 'varchar' in data_type.lower() or 'text' in data_type.lower():
                    alter_sql += " DEFAULT ''"
                # 可以根据需要添加更多数据类型的默认值处理
                else:
                    # 如果无法确定合适的默认值，可能需要手动处理或跳过
                    print(f"警告: 列 {col_name} 是 NOT NULL 且没有默认值，无法自动添加。请手动检查。")
                    continue  # 跳过此列的添加
            elif column_default is not None:
                # 确保默认值字符串被正确引用
                if isinstance(column_default, str):
                    alter_sql += f" DEFAULT '{column_default}'"
                else:
                    alter_sql += f" DEFAULT {column_default}"  # 数字等不需要引号
        else:  # is_nullable == 'YES'
            alter_sql += " NULL"
            if column_default is not None:
                if isinstance(column_default, str):
                    alter_sql += f" DEFAULT '{column_default}'"
                else:
                    alter_sql += f" DEFAULT {column_default}"
        # 添加 AUTO_INCREMENT 等额外属性
        if extra:
            alter_sql += f" {extra}"
        try:
            print(f"执行: {alter_sql}")
            cursor.execute(alter_sql)
            print(f"成功为表 {target_table} 添加列 {col_name}")
        except pymysql.Error as err:
            print(f"为表 {target_table} 添加列 {col_name} 失败: {err}")



if __name__ == '__main__':
    db = ClashDatabase()
    table_name = 'focus_players'
    reference_columns = get_table_columns(db.cursor, db.database, table_name)
    target_table_names = get_table_names(db.cursor, db.database, table_name)
    target_table_names = [name for name in target_table_names if name != table_name]

    for table_name in target_table_names:
        add_missing_columns(db.cursor, db.database, table_name, reference_columns)

    db.connection.commit()


