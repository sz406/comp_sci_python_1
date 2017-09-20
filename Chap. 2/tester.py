#Elijah Loomis
#Stock Transaction App
#show all numbers that are needed for transaction clarification

# inputs

b_shares = input('Enter number of shares purchased: ')                              #shares purchased
buy_share = input('Enter the price per share [in dollars]: ')                       #price per share bought   
buy_broker = input('Enter the commission percentage paid broker [in %]: ')          #percent paid to broker when buying 
s_shares = input('Enter the number of shares sold: ')                               #shares sold
sell_share = input('Enter the sales price per share [in dollars]: ')                #price per share sold
sell_broker = input('Enter the sales commission percentage paid broker [in %]: ')   #percent paid to broker when selling


#the math 
p1 = float(buy_broker) / 100.00
p2 = float(sell_broker) / 100.00
joe_paid = float(buy_share) * float(b_shares)                                       #joe paid         
p_com = float(joe_paid) * float(p1)                                                 #purchaced commission    
joe_sold = float(sell_share) * float(s_shares)                                      #joe sold
s_com = float(joe_sold) * p2                                                        #sold commission                                
joe_profit = float(joe_sold - joe_paid) - float(s_com + p_com)                      #joe profit

print '\n'
#output

print "Elijah Loomis's Stock Transaction App"
print 'Joe Paid: {$%:,.2f'.format(joe_paid)
print 'Purchase Commission: $%.2f' % p_com
print 'Joe sold at: $%.2f' % joe_sold 
print 'Sales Commission: $%.2f' % s_com
print "Joe's profit: $%.2f" % joe_profit
exit = input('Hit any key to Exit:')
