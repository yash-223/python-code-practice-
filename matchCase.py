color = input("Enter signal color :").lower()

match color:
    case "red":
        print("stop")
    
    case "yeelow" :
        print("ready")
    
    case "green":
        print("go")
        
    case _ :
        print("Invalid color")