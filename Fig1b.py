from Gen_Fig_Data import *;
import sys;

if __name__=="__main__":
	argv=sys.argv;
	if len(argv)==1:
		numSnpVpriv(snp_list=[i*10 for i in range(1,6)],noise=.01,bnd=.05,numSamp=1000,numStep=10000,burnIn=100000,n0=950,n1=50,type="MAF",param="");
	else:
		savename="data_for_fig/numSnp_0.01_0.05_MAF.txt"
		xlab="Number of Values Shared";
		ylab="Disclosure Risk";
		[x,y]=loadData(savename)
		drawFig(x,y,xlab,ylab)