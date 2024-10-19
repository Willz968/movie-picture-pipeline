from workspace_utils import active_session
 
with active_session():
    # do long-running work here
    while True:
        print("This loop will run forever")