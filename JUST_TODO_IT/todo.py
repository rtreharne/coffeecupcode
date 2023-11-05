import pandas as pd
from os import path
from datetime import datetime

def read_todo():
    """
    Reads the todo.csv file and returns a dataframe
    """
    # Consider what to do if fle does not exist
    if path.exists("todo_list.csv"):
        df = pd.read_csv("todo_list.csv")
        return df
        
    else:
        print("File does not exist")

def display_todo(action="LIST"):
    """
    Displays the todo list
    """
    
    df = read_todo()
    if not df.empty:  # Check if DataFrame is empty before iterating
        if action == "COMPLETED":
            df.dropna(subset=["completed_at"], inplace=True)
            df.sort_values(by="completed_at", ascending=False, inplace=True)
            for index, row in df.iterrows():
                print(index+1, row["task"])
        else:
            
            for index, row in df.iterrows():
                if pd.isnull(row["completed_at"]):
                    print(index+1, row["task"])
        
        print("\n")
                

def run_todo(action="LIST"):
    # clear console
    print("\n" * 100)
    
    # display list
    display_todo(action)


    user_input = input("TODO: ")
    
    # Quit
    if user_input == "q":
        print("Goodbye")
        return
    
    # Add task
    else:
        update_todo(user_input)

def update_todo(task):
    """
    Adds a task to the todo list
    """
    # Read todo list
    df = read_todo()

    if "DONE" in task:
        # Get integer from input
        try:
            task_id = int(task.split(" ")[1])
        except:
            print("Your request was denied")
            
        if task_id > len(df):
            print("Invalid task id")

        else:
            # Update status
            df.at[task_id-1, "completed_at"] = datetime.now()
    elif "COMPLETE" in task:
        run_todo(action="COMPLETED")
    else:
        # Create new row from task input
        new_row = pd.DataFrame({
            "task": [task],
            "created_at": [datetime.now()],
            "deleted": [False]
        })
    
        # Append new row to todo list
        df = pd.concat([df, new_row], ignore_index=True)

    # Save DataFrame to csv
    df.to_csv("todo_list.csv", index=False)

    run_todo()


if __name__ == "__main__":
    run_todo()
    
