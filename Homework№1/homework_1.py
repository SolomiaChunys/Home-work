# -*- coding: utf-8 -*-
# initializing empty envelops

necessityEnvelop = 0  # NEC, необхідні витрати
freedomEnvelop = 0    # FFA, фінансова свобода
educationEnvelop = 0  # EDU, освіта
longTermEnvelop = 0   # LTSS, резерв та на великі покупки
playEnvelop = 0       # PLAY, розваги
giveEnvelop = 0       # GIVE, подарунки

# initializing percent rate
necRate = 0.55
ffaRate = 0.1
eduRate = 0.1
ltssRate = 0.1
playRate = 0.1
giveRate = 0.05

# initializing expected income, expected necessity and other amounts
expectedIncome = 1000

sumofincome = 0
while sumofincome < expectedIncome:
    line = int(input())
    sumofincome += line

    necessityEnvelop += line * necRate
    freedomEnvelop += line * ffaRate
    educationEnvelop += line * eduRate
    longTermEnvelop += line * ltssRate
    playEnvelop += line * playRate
    giveEnvelop += line * giveRate

    print("\nEnter the amount please:")

# final output
print(f'''At the end we have:
    Necessity Envelop has:                       {str(int(necessityEnvelop))}
    Financial Freedom Envelop has:               {str(int(freedomEnvelop))}
    Education Envelop                            {str(int(educationEnvelop))}
    Long Term Saving for Spending Envelop has:   {str(int(longTermEnvelop))}
    Play Envelop has:                            {str(int(playEnvelop))}
    Give Envelop has:                            {str(int(giveEnvelop))}
    
    _______________________________________________________________
    
    Thanks for using our software :)''')

