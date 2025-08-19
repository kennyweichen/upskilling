# how to create a biased coin using a fair coin
import random
import fractions
def biasedCoin(binaryDigitStream, fairCoin):
   for d in binaryDigitStream:
      if fairCoin() != d:
         return d

def oneThird():
   while True:
      yield 0
      yield 1


def binaryDigits(fraction):
   while True:
      fraction *= 2
      yield int(fraction)
      fraction = fraction % 1


def fairCoin():
   return random.choice([0,1])

# print(binaryDigits(fractions.Fraction(1,3)))
print(sum(biasedCoin(oneThird(), fairCoin) for i in range(10000)))
print(sum(biasedCoin(binaryDigits(fractions.Fraction(1,3)), fairCoin) for i in range(10000)))

