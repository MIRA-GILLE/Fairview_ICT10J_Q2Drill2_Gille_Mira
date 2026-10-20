from pyscript import display, document

def add_member(e):
    document.getElementById("output1").innerHTML = ""
    #1
    #2
    input_member = document.getElementById("input1").value

    #assign the value to set variables
    new_member_set ={input_member}  

    #3
    all_members = members | new_member_set
    #4
    total_members = len(members | new_member_set)

    #display the items in ascending order (A-Z) seperated by br
    member_list = "<br>".join(sorted(all_members))

    #display
    document.getElementById("output1").innerHTML = f'All Members: <br> {member_list}'
    display(f'Total Members: {total_members}', target = "output1")
