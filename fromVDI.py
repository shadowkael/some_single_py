def walk_system_call_list():
    for system_call in SYSTEM_CALL_LIST:
        process_dir = ROOT_DIR + system_call + "\\sys_tree"
        if os.path.isdir(process_dir):
            os.chdir(process_dir)
        else:
            continue
        log_line = dict()
        vertices = list()
        for log_and_sys_tree in sorted(os.listdir(os.getcwd())):
            if not os.path.isfile(os.getcwd() + "\\" + log_and_sys_tree):
                continue
            # count every weight of sys_tree and store in log_line
            if log_and_sys_tree.endswith("log"):
                log_line[log_and_sys_tree.split('_')[0]] = get_line_num(log_and_sys_tree)
            # write contact of vertices
            elif log_and_sys_tree.startswith('sys'):
                vertices.extend(generate_vertices(log_and_sys_tree))
        # generate vertices and write in file
        vertices_unique = list(set(vertices))
        vertices_unique.sort(key=vertices.index)

        # write file head and point info
        target_file_name = 'Matrix_' + system_call + '.net'
        write_file_head(target_file_name, len(vertices_unique))
        write_file_point(target_file_name, vertices_unique)

        # init matrix with '0'
        init_matrix = generate_init_matrix(len(vertices_unique))
        result_matrix = list()
        result_matrix.extend(init_matrix)
        for log_and_sys_tree in sorted(os.listdir(os.getcwd())):
            if not os.path.isfile(os.getcwd() + "\\" + log_and_sys_tree):
                continue
            if log_and_sys_tree.startswith('sys'):
                sys_tree_num = log_and_sys_tree.split('_')[-1]
                data_format_matrix(log_and_sys_tree, log_line[sys_tree_num], vertices_unique,
                                   result_matrix)
        write_file_matrix(target_file_name, init_matrix)

def walk_cwd_file():
    cwd = os.getcwd()
    for cwd_sub in os.listdir(cwd):
        if os.path.isfile(cwd_sub):
            pass

def get_hash_name(filename):
    return filename