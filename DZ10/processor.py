from datetime import datetime as dt
import logging

def t():
    return dt.now().strftime('%D\t%H:%M:%S')


logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    handlers=[
        logging.FileHandler("my_log.log", encoding='utf-8', mode='w')],
    level=logging.INFO,
)


# def write_log(*params):
#     with open("logg.txt", 'w', encoding='utf-8') as logfile:
#         logfile.write('\t'.join(list(map(lambda x: str(x), params)))+'\n')


def check_4_win(fld: list):
    win_coord = ((0, 1, 2),
                (1,2,3),
                (4,5,6),
                (5,6,7),
                (8,9,10),
                (9,10,11),
                (12,13,14),
                (13,14,15),
                (0,4,8),
                (4,8,12),
                (1,5,9),
                (5,9,13),
                (2,6,10),
                (6,10,14),
                (3,7,11),
                (7,11,15),
                (4,9,14),
                (0,5,10),
                (5,10,15),
                (1,6,11),
                (2,5,8),
                (3,6,9),
                (6,9,12),
                (7,10,13))
 # сравниваем текущее поле с выигрышными комбинациями
    for winrec in win_coord:                                
        if (fld[winrec[0]] == fld[winrec[1]] == fld[winrec[2]]) and fld[winrec[0]] != ' ':
            return True
    return False

def isfull(fld: list):
    for itm in fld:
        if itm == ' ':
            return False
    return True   


if __name__ == '__main__':
    pass