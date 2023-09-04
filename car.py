class Car:
    def __init__(self):
        self.name = 'Toyota Corolla'
        print(f'Hello!\nYou just entered an Automatic geared {self.name} car.\nPress ENTER to start the car')
        self.start()
    
    def drive(self):
        print(f'\nYou are now driving a {self.name} car')
    
    def reverse(self):
        print(f'You are now reversing your {self.name} car')
    
    def park(self):
        print(f'You are about to park your {self.name} car')
    
    def start(self):
        res = input('')
        if res == '':
            print(f'Hello!\nThe car has started.\n\nPress D to Drive\nPress R to Reverse\nPress P to Park')
            choice = input('').capitalize()
            if choice == 'D':
                self.drive()
            elif choice == 'R':
                self.reverse()
            elif choice == 'P':
                self.park()
            else:
                print('Quit Operation!\nYour car has knocked.')
        else:
            Car()
    
    
Car()