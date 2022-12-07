# programming_dictionary = {
#     "Bug": "In computer technology, a bug is a coding error in a computer program. We consider a program to also include the microcode that is manufactured into a microprocessor.",
#     "Command": "In the Python programming language, commands basically refer to different functions or methods that we can execute on the python shell to work them as commands.",
#     "Programmer": "A programmer is an individual that writes/creates computer software or applications by giving the computer specific programming instructions."
# }

# # add item to programming_dictionary
# programming_dictionary["Python"] = "Python is commonly used for developing websites and software, task automation, data analysis, and data visualization. Since it's relatively easy to learn, Python has been adopted by many non-programmers such as accountants and scientists, for a variety of everyday tasks, like organizing finances"

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

bd_division_info = {
    "Barisal": {
                "District": 6,
                "Upazilla": 39,
                "Council": 333,
            },
    "Chittagong": {
                "District": 11,
                "Upazilla": 97,
                "Council": 336,
    }
}
print(bd_division_info["Barisal"] ["District"])