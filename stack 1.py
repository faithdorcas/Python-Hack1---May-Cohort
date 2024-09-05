def reverse_string(s: str) -> str:
    stack = []
    
    # Push all characters onto the stack
    for char in s:
        stack.append(char)
    
    # Pop all characters to reverse the string
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Example usage
s = "hello"
print(reverse_string(s))  # Output: "olleh"