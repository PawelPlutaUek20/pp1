import re
ciag_znakow='12903m80hFCB8324cmTfsONAJnkdLEPfsd2382u4j328jd0239jSZY()#KL!asd@$dsaUB#%^*'
def wielkie_litery():
    print(re.findall('[A-Z]',ciag_znakow))
wielkie_litery()