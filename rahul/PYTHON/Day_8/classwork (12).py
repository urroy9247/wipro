def greeting(first, last):
      # nested helper function
      def getFullName():
            return first + " " + last
      print("Hi, " + getFullName() + "!")
 
greeting('Quincy', 'Larson')
 