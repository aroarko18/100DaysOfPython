inputs = [] 
lenghts = []
heights = []

trip_count = 0
total_length = 0
total_height = 0
while True: 
    
    trip = input('Enter the trip/mountain name : ') 

    if trip != 'END':
        length = float(input("Length of trip in km : "))
        lenghts.append(length)

        height = float(input("Vertical climb of trip : "))
        heights.append(height)
    
    if trip == 'END':
        # trip inputs
        print("Total Trip : ")
        for all_trip in inputs:
            trip_count = trip_count + 1
            print(str(trip_count) + ". " + all_trip)
        
        # length inputs
        for all_length in lenghts:
            total_length += all_length
            # print(total_length)
        
        # vertical inputs
        for all_height in heights:
            total_height += all_height
            # print(total_height)
        break

    else:
        inputs.append(trip)
         

print(f"Total length in km : {total_length}")
print(f"Vertical climb trip : {total_height}") 

# print(inputs) # display the list.
# print(lenghts)
# print(heights)