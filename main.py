from pyscript import display, document

def add_member(e):
    document.getElementById("output1").innerHTML = ""
    #1
    members = {'Alice', 'Bob', 'Charlie'}
    #2
    input_first_name = document.getElementById("input1").value
    input_last_name = document.getElementById("input2").value

    #assign the value to set variables
    new_member_set ={f"{input_last_name} {input_first_name}"}  

    #3
    all_members = members | new_member_set
    #4
    total_members = len(members | new_member_set)

    #display the items in ascending order (A-Z) seperated by br
    member_list = "<br>".join(sorted(all_members))

    #display
    document.getElementById("output1").innerHTML = f'All Members: <br> {member_list}'
    display(f'Total Members: {total_members}', target = "output1")
