#!/usr/bin/env python

def count_words(file_contents):
    return len(file_contents.split())
    
def count_chars(file_contents):
    chars = {}
    for char in file_contents.lower():
        if char not in chars.keys():
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def create_report(file_contents, path):
    report = f"--- Begin report of {path} ---\n{count_words(file_contents)} words found in the document\n\n"
    chars_dict = count_chars(file_contents)
    for w in sorted(chars_dict, key=chars_dict.get, reverse=True):
        if w.isalpha():
            report += f"The `{w}` character was found {chars_dict[w]} times\n"
    report += "--- End report ---"
    return report


if __name__ == '__main__':
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        print(create_report(file_contents, "books/frankenstein.txt"))