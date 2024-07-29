def generate_network_file(network_file, LIs, filter_seq):
    with open(network_file, 'a+') as f:
        h = 0
        while h < len(filter_seq):
            y = filter_seq[h]  # 把sq_ls里的元素一个一个提出来
            kl1 = LIs.index(y)  # 找到sq_ls里的元素在大数据库LIs里的位置
            thg = []
            for et in LIs:
                if et[0] == y[0] and et[1] == y[1] and et[2] == y[2] and et[3] == y[3] and et[4] == y[4] and et[5] == y[5] and et[6] == y[6] and et[7] == y[7]:
                    loc = LIs.index(et)
                    thg.append(loc)  # 找出来跟待检测的数据列表长的一模一样的元素所在的位置,注意不一定只有待检测数据自己，病毒平传也是有可能的。
            
            LIs_use = [LIs[df] for df in range(0, len(LIs), 1) if df not in thg]  # 剔除与待检测的数据一模一样的元素，组成一个新的列表LIs_use
            print(f'第{h + 1}个数据点所在大数据库里的位置是{kl1 + 1}')
            
            i = 0
            aList = []
            while i < 8:  # 从这里开始去检查sq_ls里提出来的元素满足构建网络条件的节点
                for k in LIs_use:
                    if k[i] == y[i] and abs(k[8] - y[8]) < 1:  # k[i] == y[i]的意思是任意一个segment一样;abs(k[8]-y[8])<1的意思是时间相差<1年
                        aList.append(k)  # 符合条件的列表统统追加到列表aList里
                i += 1  # 循环8次,逐个检查每个segment:[]
            
            temp = []
            for dd in aList:  # 这个操作是去重
                if dd not in temp:  # 这里做了一个很简单的判断~
                    temp.append(dd)
            
            for z in temp:
                f.write(f'{y}|{z}')
                f.write("\n")
            
            h += 1
