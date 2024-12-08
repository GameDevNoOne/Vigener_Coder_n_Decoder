from Vigenere_Table_Generator import *

Keyword_1 = "Covarubis"
Keyword_2 = "Paswrd"
Message = "Hello "
def Test():
    diff_Table = Diff_Table(["A", "B", "C"])
    print(diff_Table)
    assert(diff_Table == {'A' : 0, 'B' : 1, 'C' : 2})

def Test_Encode():
    Encoded_Message = Encode_Message(Keyword_1, Keyword_2, Message)
    print(Encoded_Message)
    assert Encoded_Message == "ZŠXRVF", "Message je {}".format(Encoded_Message)
if __name__ == "__main__":
    Test_Encode()