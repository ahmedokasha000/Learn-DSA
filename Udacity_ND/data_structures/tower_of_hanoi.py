def tower_of_Hanoi(num_disks, source, auxilary, destination):
    if num_disks > 0:
        tower_of_Hanoi(num_disks-1, source, destination, auxilary)
        print(f"{source} to {destination}")
        tower_of_Hanoi(num_disks-1, auxilary, source , destination)