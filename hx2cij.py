import argparse

def max_let(let1, let2):
    if 'R' in [let1,let2]:
        return 'R'
    elif 'G' in [let1,let2]:
        return 'G'
    else:
        return 'B'

def hx2cij(hxfile,cijfile,output):
    #get hx data
    hx_data = []
    with open(hxfile) as hx:
        for line in hx:
            line = line.strip()
            hx_data.append(line.split())
    hx.close()
    #get cij data
    cij_data = []
    with open(cijfile) as cij:
        for line in cij:
            line = line.strip()
            cij_data.append(line.split())
    cij.close()
    #find all contacts in cij where both residues have hx data
    contacts = []
    for [i,j,x] in cij_data:
        is_hx = [False,False]
        for [k, let] in hx_data:
            if i == k:
                is_hx[0] = True
                i_let = let
            if j == k:
                is_hx[1] = True
                j_let = let
        if is_hx == [True,True]:
            contacts.append([i,j,max_let(i_let,j_let)])
    #write out those contacts
    out = open(output,'w+')
    for c in contacts:
        out.write("%4i %4i %s\n"%(int(c[0]),int(c[1]),c[2]))
    out.close()

def main():
    parser = argparse.ArgumentParser(description="Convert a list of early, intermediate, and late folding residues into an age-based contact map")
    #hxfile
    parser.add_argument('-hx',metavar='file.hx',dest='hxfile',nargs=1,help='file containing the list of residues')
    #cijfile
    parser.add_argument('-cij',metavar='file.cij',dest='cijfile',nargs=1,help='file containing protein contact map')
    #output
    parser.add_argument('-o',metavar='file.hxcij',dest='output',nargs=1,help='Output contact map')
    args=parser.parse_args()
    hx2cij(args.hxfile[0],args.cijfile[0],args.output[0])

if __name__ == '__main__':
    main()
