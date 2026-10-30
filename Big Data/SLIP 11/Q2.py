# 2. Consider the Customer order Data set. Write a Map Reduce program to find the amount spent by each customer.


from mrjob.job import MRJob

class MRCustomerOrders(MRJob):
    def mapper(self, key, line):
        (customerID, productID, amount) = line.split(",")

        yield customerID, float(amount)

    def reducer(self, customerID, amounts):
        total = 0

        for amount in amounts:
            total += amount

        yield customerID, total

if __name__ == '__main__':
    MRCustomerOrders.run()