#!/usr/bin/env python
# coding: utf-8

# In[17]:


num_1 = int(input("Digite 1º numero: "))
num_2 = int(input("Digite 2º numero: "))
num_3 = int(input("Digite 3º numero: "))
num_4 = int(input("Digite 4º numero: "))
num_5 = int(input("Digite 5º numero: "))

#ordem = input("Qual ordem você deseja? d-decrescente c- Crescente : ")

### Ordem decrescente 

if num_1 > num_2 and num_1 > num_3 and num_1 > num_4 and num_4 > num_5:
    if num_2 > num_3 and num_2 > num_4 and num_2 > num_5:
        if num_3 > num_4 and num_3 > num_5:
            if num_4 > num_5:
                print(f'nº {num_1} nº {num_2} nº{num_3} nº {num_4} nº {num_5}')
            else:
                print(f'nº {num_1} nº {num_2} nº{num_3} nº {num_5} nº {num_4}')
        else:
            print(f'nº {num_1} nº {num_2} nº{num_4} nº {num_3} nº {num_5}')
    else:
        print(f'nº {num_1} nº {num_2} nº{num_4} nº {num_5} nº {num_3}')
#############################################################################                
if num_2 > num_1 and num_2 > num_3 and num_2 > num_4 and num_2 > num_5:
    if num_1 > num_3 and num_1 > num_4 and num_1 > num_5:
        if num_3 > num_4 and num_3 > num_5:
            if num_4 > num_5:
                print(f'nº {num_2} nº {num_1} nº{num_3} nº {num_4} nº {num_5}')
            else:
                print(f'nº {num_2} nº {num_1} nº{num_3} nº {num_5} nº {num_4}')
        else:
            print(f'nº {num_2} nº {num_1} nº{num_4} nº {num_3} nº {num_5}')
    else:
        print(f'nº {num_2} nº {num_1} nº{num_4} nº {num_5} nº {num_3}')
##############################################################################
if num_3 > num_1 and num_3 > num_2 and num_3 > num_4 and num_3 > num_5:
    if num_1 > num_2 and num_1 > num_4 > num_1 > num_5:
        if num_2 > num_4 and num_2 > num_5:
            if num_4 > num_5:
                print(f'nº {num_3} nº {num_1} nº{num_2} nº {num_4} nº {num_5}')
            else:
                print(f'nº {num_3} nº {num_2} nº{num_1} nº {num_5} nº {num_4}')
        else:
            print(f'nº {num_3} nº {num_2} nº{num_4} nº {num_1} nº {num_5}')
    else:
        print(f'nº {num_3} nº {num_2} nº{num_4} nº {num_5} nº {num_1}')
###############################################################################
if num_4 > num_1 and num_4 > num_2 and num_4 > num_3 and num_4 > num_5:
    if num_1 > num_2 and num_1 > num_3 > num_1 > num_5:
        if num_2 > num_3 and num_2 > num_5:
            if num_3 > num_5:
                print(f'nº {num_4} nº {num_1} nº{num_2} nº {num_3} nº {num_5}')
            else:
                print(f'nº {num_4} nº {num_2} nº{num_3} nº {num_5} nº {num_1}')
        else:
            print(f'nº {num_4} nº {num_2} nº{num_1} nº {num_3} nº {num_5}')
    else:
        print(f'nº {num_4} nº {num_2} nº{num_1} nº {num_5} nº {num_3}')
                
###############################################################################
if num_5 > num_1 and num_5 > num_2 and num_5 > num_3 and num_5 > num_4:
    if num_1 > num_2 and num_1 > num_3 > num_1 > num_4:
        if num_2 > num_3 and num_2 > num_4:
            if num_3 > num_4:
                print(f'nº {num_5} nº {num_1} nº{num_2} nº {num_3} nº {num_4}')
            else:
                print(f'nº {num_5} nº {num_2} nº{num_3} nº {num_1} nº {num_4}')
        else:
            print(f'nº {num_5} nº {num_2} nº{num_4} nº {num_3} nº {num_1}')
    else:
        print(f'nº {num_5} nº {num_2} nº{num_4} nº {num_1} nº {num_3}')


# In[ ]:




