def print_string_frame(s):
    # Determine the width for each column (based on the largest index)
    max_index_width = max(len(str(len(s)-1)), len(str(-len(s))))
    column_width = max_index_width + 2  # Adding extra space for padding
    
    # Build the top and bottom frame lines
    frame_line = '+' + '+'.join(['-' * column_width for _ in range(len(s))]) + '+'
    
    # Build the negative indices row
    neg_indices = '|' + '|'.join([f'{i-len(s):^{column_width}}' for i in range(len(s))]) + '|'
    
    # Build the string characters row
    chars = '|' + '|'.join([f'{char:^{column_width}}' for char in s]) + '|'
    
    # Build the positive indices row
    pos_indices = '|' + '|'.join([f'{i:^{column_width}}' for i in range(len(s))]) + '|'
    
    # Print the framed output
    print()
    print(frame_line)
    print(neg_indices)
    print(frame_line)
    print(chars)
    print(frame_line)
    print(pos_indices)
    print(frame_line)
    print()
