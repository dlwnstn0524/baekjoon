def solution(word):
    answer = 0
    
    char_list = ['A', 'E', 'I', 'O', 'U']
    root = ""
    order_dict = dict()

    def calculate_seq_num(parent_node, last_num):
        seq_num = last_num
        if len(parent_node) == 5:
            return last_num
        for character in char_list:
            seq_num += 1
            current = parent_node + character
            order_dict[current] = seq_num

            seq_num = calculate_seq_num(current, seq_num)
        return seq_num

    calculate_seq_num(root, 0)
    
    answer = order_dict[word]
        
    return answer