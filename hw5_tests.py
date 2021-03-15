#########################################
##### Name: Hongyu Dai              #####
##### Uniqname:hongyud              #####
#########################################
import unittest
import hw5_cards

class TestCard(unittest.TestCase):

    def test_construct_Card(self):
        c1 = hw5_cards.Card(0, 2)
        c2 = hw5_cards.Card(1, 1)

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")
        self.assertEqual(c1.rank, 2)
        self.assertEqual(c1.rank_name, "2")

        self.assertIsInstance(c1.suit, int)
        self.assertIsInstance(c1.suit_name, str)
        self.assertIsInstance(c1.rank, int)
        self.assertIsInstance(c1.rank_name, str)

        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")
        
    def test_q1(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card with rank 12, its rank_name will be "Queen"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c_q1 = hw5_cards.Card(rank = 12)
        self.assertEqual(c_q1.rank_name, "Queen")
        
        X = c_q1.rank_name
        Y = "Queen"
        return X, Y
    
    def test_q2(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c_q2 = hw5_cards.Card(suit = 1)
        self.assertEqual(c_q2.suit_name, "Clubs")
        
        X = c_q2.suit_name
        Y = "Clubs"
        return X, Y    
    

    def test_q3(self):
        '''
        1. fill in your test method for question 3:
        Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c_q3 = hw5_cards.Card(suit = 3,rank = 13)
        self.assertEqual(c_q3.__str__(), "King of Spades")
        X = c_q3.__str__() 
        Y = "King of Spades"
        return X, Y
    
    def test_q4(self):
        '''
        1. fill in your test method for question 4:
        Test that if you create a deck instance, it will have 52 cards in its cards instance variable
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        
        q4 = hw5_cards.Deck()
        len_q4 = len(q4.cards)
        self.assertEqual(len_q4, 52)
        X = len_q4
        Y = 52
        return X, Y  

    def test_q5(self):
        '''
        1. fill in your test method for question 5:
        Test that if you invoke the deal_card method on a deck, it will return a card instance.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q5 = hw5_cards.Deck().deal_card()
        self.assertIsInstance(q5,hw5_cards.Card)
        X = q5
        Y = hw5_cards.Card
        return X, Y
    
    def test_q6(self):
        '''
        1. fill in your test method for question 6:
        
        Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q6_Deck = hw5_cards.Deck()
        len_before = len(q6_Deck.cards)

        q6_Deck.deal_card()
        len_after = len(q6_Deck.cards)
        self.assertEqual(len_before-1, len_after)
        
        X = len_before-1
        Y = len_after
        return X, Y    
    

    def test_q7(self):
        '''
        1. fill in your test method for question 7:
        Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q7_Deck = hw5_cards.Deck()

        removed = q7_Deck.cards[-1]
        q7_Deck.deal_card(i=-1)
        
        before = q7_Deck.cards
        len_before = len(before)

        q7_Deck.replace_card(removed)
        after = q7_Deck.cards
        len_after = len(after)

        self.assertEqual(len_before+1, len_after)
        Z = len_before + 1
        X = len_before + 1
        Y = len_after
        return Z,X,Y
    
    def test_q8(self):
        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        
        c1 = hw5_cards.Card(0, 2)
        c2 = hw5_cards.Card(1, 1)
        q8_Deck = hw5_cards.Deck()

        add = q8_Deck.cards[0]

        q8_Deck.deal_card(i=-1)
        before = q8_Deck.cards
        len_before = len(before)

        q8_Deck.replace_card(add)
        after = q8_Deck.cards
        len_after = len(after)

        self.assertEqual(len_before, len_after)
        X = len_before + 1
        Y = len_after + 1
        return X, Y  



if __name__=="__main__":
    unittest.main()