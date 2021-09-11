class Category:

    def __init__(self,name):
        self.name= name
        self.ledger=list()

    def __str__(self):
        tite=f"{self.name:*^30}\n"
        items=""
        tot=0
        for item in self.ledger:
            items += f"{item['description'] [0:23]:23}" + f"{item['amount'] :>7.2f}" + '\n'
            tot += item['amount']

        output = tite + items +"Total:" +" "+ str(tot)
        return output

    def deposit(self, amount ,description=""):
        self.ledger.append({"amount":amount ,"description":description})



    def withdraw(self, amount ,description=""):

         if(self.check_funds(amount)):
            self.ledger.append({"amount": -amount ,"description":description})
            return True
         return False

    def get_balance(self):
        tot_cash=0
        for item in self.ledger:
            tot_cash += item["amount"]
        return tot_cash


    def transfer(self, amount,category):

        if(self.check_funds(amount)):
            self.withdraw(amount,"Transfer to" +" "+ category.name)
            category.deposit(amount,"Transfer from" +" "+ self.name)
            return True
        return False

    def check_funds(self,amount):

        if(self.get_balance()>=amount):
            return True
        return False


def create_spend_chart(categories):
  category_names = []
  spent = []
  spent_percentages = []

  for category in categories:
    total = 0
    for item in category.ledger:
      if item['amount'] < 0:
        total -= item['amount']
    spent.append(round(total, 2))
    category_names.append(category.name)

  for amount in spent:
    spent_percentages.append(round(amount / sum(spent), 2)*100)

  graph = "Percentage spent by category\n"

  labels = range(100, -10, -10)

  for label in labels:
    graph += str(label).rjust(3) + "| "
    for percent in spent_percentages:
      if percent >= label:
        graph += "o  "
      else:
        graph += "   "
    graph += "\n"

  graph += "    ----" + ("---" * (len(category_names) - 1))
  graph += "\n     "

  longest_name_length = 0

  for name in category_names:
    if longest_name_length < len(name):
      longest_name_length = len(name)

  for i in range(longest_name_length):
    for name in category_names:
      if len(name) > i:
        graph += name[i] + "  "
      else:
        graph += "   "
    if i < longest_name_length-1:
      graph += "\n     "



  return(graph)






