import os
import subprocess
import sys

deltext=""
if sys.platform.startswith("linux")  :
	deltext="rm"
	copytext="cp"
if sys.platform.startswith("darwin")  :
	deltext="rm"
	copytext="cp"
if sys.platform.startswith("win") :
	deltext="del"
	copytext="copy"

def run_in_shell(cmd):
    subprocess.check_call(cmd, shell=True)

def replace(namefile,oldtext,newtext):
	f = open(namefile,'r')
	filedata = f.read()
	f.close()

	newdata = filedata.replace(oldtext,newtext)

	f = open(namefile,'w')
	f.write(newdata)
	f.close()


def rsaset(tb,tff,nb,base,ml) :
	bd="B"+tb+"_"+base
	fnameh="config_big_"+bd+".h"
	run_in_shell(copytext+" config_big.h "+fnameh)
	replace(fnameh,"XXX",bd)
	replace(fnameh,"@NB@",nb)
	replace(fnameh,"@BASE@",base)

	fnameh="config_ff_"+tff+".h"
	run_in_shell(copytext+" config_ff.h "+fnameh)
	replace(fnameh,"XXX",bd)
	replace(fnameh,"WWW",tff)
	replace(fnameh,"@ML@",ml)

	fnamec="big_"+bd+".cpp"
	fnameh="big_"+bd+".h"

	run_in_shell(copytext+" big.cpp "+fnamec)
	run_in_shell(copytext+" big.h "+fnameh)

	replace(fnamec,"XXX",bd)
	replace(fnameh,"XXX",bd)
	run_in_shell("g++ -O3 -c "+fnamec)

	fnamec="ff_"+tff+".cpp"
	fnameh="ff_"+tff+".h"

	run_in_shell(copytext+" ff.cpp "+fnamec)
	run_in_shell(copytext+" ff.h "+fnameh)

	replace(fnamec,"WWW",tff)
	replace(fnamec,"XXX",bd)
	replace(fnameh,"WWW",tff)
	replace(fnameh,"XXX",bd)
	run_in_shell("g++ -O3 -c "+fnamec)

	fnamec="rsa_"+tff+".cpp"
	fnameh="rsa_"+tff+".h"

	run_in_shell(copytext+" rsa.cpp "+fnamec)
	run_in_shell(copytext+" rsa.h "+fnameh)

	replace(fnamec,"WWW",tff)
	replace(fnamec,"XXX",bd)
	replace(fnameh,"WWW",tff)
	replace(fnameh,"XXX",bd)
	run_in_shell("g++ -O3 -c "+fnamec)

def curveset(tb,tf,tc,nb,base,nbt,m8,mt,ct,pf,stw,sx,ab,cs) :
	bd="B"+tb+"_"+base
	fnameh="config_big_"+bd+".h"
	run_in_shell(copytext+" config_big.h "+fnameh)
	replace(fnameh,"XXX",bd)
	replace(fnameh,"@NB@",nb)
	replace(fnameh,"@BASE@",base)

	fnameh="config_field_"+tf+".h"
	run_in_shell(copytext+" config_field.h "+fnameh)
	replace(fnameh,"XXX",bd)
	replace(fnameh,"YYY",tf)
	replace(fnameh,"@NBT@",nbt)
	replace(fnameh,"@M8@",m8)
	replace(fnameh,"@MT@",mt)

	ib=int(base)
	inb=int(nb)
	inbt=int(nbt)
	sh=ib*(1+((8*inb-1)//ib))-inbt

	if sh > 6 :
		sh=6
	replace(fnameh,"@SH@",str(sh))

	fnameh="config_curve_"+tc+".h"
	run_in_shell(copytext+" config_curve.h "+fnameh)
	replace(fnameh,"XXX",bd)
	replace(fnameh,"YYY",tf)
	replace(fnameh,"ZZZ",tc)
	replace(fnameh,"@CT@",ct)
	replace(fnameh,"@PF@",pf)

	replace(fnameh,"@ST@",stw)
	replace(fnameh,"@SX@",sx)
	replace(fnameh,"@CS@",cs)
	replace(fnameh,"@AB@",ab)


	fnamec="big_"+bd+".cpp"
	fnameh="big_"+bd+".h"

	run_in_shell(copytext+" big.cpp "+fnamec)
	run_in_shell(copytext+" big.h "+fnameh)

	replace(fnamec,"XXX",bd)
	replace(fnameh,"XXX",bd)
	run_in_shell("g++ -O3 -c "+fnamec)

	fnamec="fp_"+tf+".cpp"
	fnameh="fp_"+tf+".h"

	run_in_shell(copytext+" fp.cpp "+fnamec)
	run_in_shell(copytext+" fp.h "+fnameh)

	replace(fnamec,"YYY",tf)
	replace(fnamec,"XXX",bd)
	replace(fnameh,"YYY",tf)
	replace(fnameh,"XXX",bd)
	run_in_shell("g++ -O3 -c "+fnamec)

	run_in_shell("g++ -O3 -c rom_field_"+tf+".cpp")

	fnamec="ecp_"+tc+".cpp"
	fnameh="ecp_"+tc+".h"

	run_in_shell(copytext+" ecp.cpp "+fnamec)
	run_in_shell(copytext+" ecp.h "+fnameh)

	replace(fnamec,"ZZZ",tc)
	replace(fnamec,"YYY",tf)
	replace(fnamec,"XXX",bd)
	replace(fnameh,"ZZZ",tc)
	replace(fnameh,"YYY",tf)
	replace(fnameh,"XXX",bd)
	run_in_shell("g++ -O3 -c "+fnamec)

	fnamec="ecdh_"+tc+".cpp"
	fnameh="ecdh_"+tc+".h"

	run_in_shell(copytext+" ecdh.cpp "+fnamec)
	run_in_shell(copytext+" ecdh.h "+fnameh)

	replace(fnamec,"ZZZ",tc)
	replace(fnamec,"YYY",tf)
	replace(fnamec,"XXX",bd)
	replace(fnameh,"ZZZ",tc)
	replace(fnameh,"YYY",tf)
	replace(fnameh,"XXX",bd)
	run_in_shell("g++ -O3 -c "+fnamec)

	run_in_shell("g++ -O3 -c rom_curve_"+tc+".cpp")

	if pf != "NOT" :
		fnamec="fp2_"+tf+".cpp"
		fnameh="fp2_"+tf+".h"

		run_in_shell(copytext+" fp2.cpp "+fnamec)
		run_in_shell(copytext+" fp2.h "+fnameh)
		replace(fnamec,"YYY",tf)
		replace(fnamec,"XXX",bd)
		replace(fnameh,"YYY",tf)
		replace(fnameh,"XXX",bd)
		run_in_shell("g++ -O3 -c "+fnamec)

		fnamec="fp4_"+tf+".cpp"
		fnameh="fp4_"+tf+".h"

		run_in_shell(copytext+" fp4.cpp "+fnamec)
		run_in_shell(copytext+" fp4.h "+fnameh)
		replace(fnamec,"YYY",tf)
		replace(fnamec,"XXX",bd)
		replace(fnamec,"ZZZ",tc)
		replace(fnameh,"YYY",tf)
		replace(fnameh,"XXX",bd)
		replace(fnameh,"ZZZ",tc)
		run_in_shell("g++ -O3 -c "+fnamec)

		fnamec="fp12_"+tf+".cpp"
		fnameh="fp12_"+tf+".h"

		run_in_shell(copytext+" fp12.cpp "+fnamec)
		run_in_shell(copytext+" fp12.h "+fnameh)
		replace(fnamec,"YYY",tf)
		replace(fnamec,"XXX",bd)
		replace(fnamec,"ZZZ",tc)
		replace(fnameh,"YYY",tf)
		replace(fnameh,"XXX",bd)
		replace(fnameh,"ZZZ",tc)
		run_in_shell("g++ -O3 -c "+fnamec)

		fnamec="ecp2_"+tc+".cpp"
		fnameh="ecp2_"+tc+".h"

		run_in_shell(copytext+" ecp2.cpp "+fnamec)
		run_in_shell(copytext+" ecp2.h "+fnameh)
		replace(fnamec,"ZZZ",tc)
		replace(fnamec,"YYY",tf)
		replace(fnamec,"XXX",bd)
		replace(fnameh,"ZZZ",tc)
		replace(fnameh,"YYY",tf)
		replace(fnameh,"XXX",bd)
		run_in_shell("g++ -O3 -c "+fnamec)

		fnamec="pair_"+tc+".cpp"
		fnameh="pair_"+tc+".h"

		run_in_shell(copytext+" pair.cpp "+fnamec)
		run_in_shell(copytext+" pair.h "+fnameh)
		replace(fnamec,"ZZZ",tc)
		replace(fnamec,"YYY",tf)
		replace(fnamec,"XXX",bd)
		replace(fnameh,"ZZZ",tc)
		replace(fnameh,"YYY",tf)
		replace(fnameh,"XXX",bd)
		run_in_shell("g++ -O3 -c "+fnamec)

		fnamec="mpin_"+tc+".cpp"
		fnameh="mpin_"+tc+".h"

		run_in_shell(copytext+" mpin.cpp "+fnamec)
		run_in_shell(copytext+" mpin.h "+fnameh)
		replace(fnamec,"ZZZ",tc)
		replace(fnamec,"YYY",tf)
		replace(fnamec,"XXX",bd)
		replace(fnameh,"ZZZ",tc)
		replace(fnameh,"YYY",tf)
		replace(fnameh,"XXX",bd)
		run_in_shell("g++ -O3 -c "+fnamec)

		fnamec="bls_"+tc+".cpp"
		fnameh="bls_"+tc+".h"

		run_in_shell(copytext+" bls.cpp "+fnamec)
		run_in_shell(copytext+" bls.h "+fnameh)
		replace(fnamec,"ZZZ",tc)
		replace(fnamec,"YYY",tf)
		replace(fnamec,"XXX",bd)
		replace(fnameh,"ZZZ",tc)
		replace(fnameh,"YYY",tf)
		replace(fnameh,"XXX",bd)
		run_in_shell("g++ -O3 -c "+fnamec)



replace("arch.h","@WL@","16")
print("Elliptic Curves")
print("1. ED25519")
print("2. NUMS256E")

print("Pairing-Friendly Elliptic Curves")
print("3. BN254")
print("4. BN254CX")

print("RSA")
print("5. RSA2048")


selection=[]
ptr=0
max=6

curve_selected=False
pfcurve_selected=False
rsa_selected=False

while ptr<max:
	x=int(input("Choose a Scheme to support - 0 to finish: "))
	if x == 0:
		break
#	print("Choice= ",x)
	already=False
	for i in range(0,ptr):
		if x==selection[i]:
			already=True
			break
	if already:
		continue

	selection.append(x)
	ptr=ptr+1

# curveset(big,field,curve,big_length_bytes,bits_in_base,modulus_bits,modulus_mod_8,modulus_type,curve_type,pairing_friendly,sextic twist,sign of x,ate bits,curve security)
# for each curve give names for big, field and curve. In many cases the latter two will be the same.
# Typically "big" is the size in bits, always a multiple of 8, "field" describes the modulus, and "curve" is the common name for the elliptic curve
# big_length_bytes is "big" divided by 8
# Next give the number base used for 16 bit architectures, as n where the base is 2^n (note that these must be fixed for the same "big" name, if is ever re-used for another curve)
# modulus_bits is the bit length of the modulus, typically the same or slightly smaller than "big"
# modulus_mod_8 is the remainder when the modulus is divided by 8
# modulus_type is NOT_SPECIAL, or PSEUDO_MERSENNE, or MONTGOMERY_Friendly, or GENERALISED_MERSENNE (supported for GOLDILOCKS only)
# curve_type is WEIERSTRASS, EDWARDS or MONTGOMERY
# pairing_friendly is BN, BLS or NOT (if not pairing friendly)
# ate bits is number of bits in Ate parameter (from romgen program)
# if pairing friendly. M or D type twist, and sign of the family parameter x


	if x==1:
		curveset("256","F25519","ED25519","32","13","255","5","PSEUDO_MERSENNE","EDWARDS","NOT","","","","128")
		curve_selected=True
	if x==2:
		curveset("256","F256PME","NUMS256E","32","13","256","3","PSEUDO_MERSENNE","EDWARDS","NOT","","","","128")
		curve_selected=True


	if x==3:
		curveset("256","BN254","BN254","32","13","254","3","NOT_SPECIAL","WEIERSTRASS","BN","D_TYPE","NEGATIVEX","66","128")
		pfcurve_selected=True
	if x==4:
		curveset("256","BN254CX","BN254CX","32","13","254","3","NOT_SPECIAL","WEIERSTRASS","BN","D_TYPE","NEGATIVEX","66","128")
		pfcurve_selected=True

# rsaset(big,ring,big_length_bytes,bits_in_base,multiplier)
# for each choice give distinct names for "big" and "ring".
# Typically "big" is the length in bits of the underlying big number type
# "ring" is the RSA modulus size = "big" times 2^m
# big_length_bytes is "big" divided by 8
# Next give the number base used for 16 bit architectures, as n where the base is 2^n
# multiplier is 2^m (see above)

# There are choices here, different ways of getting the same result, but some faster than others
	if x==5:
		#256 is slower but may allow reuse of 256-bit BIGs used for elliptic curve
		#512 is faster.. but best is 1024
		rsaset("256","RSA2048","32","13","8")
		rsa_selected=True


run_in_shell(deltext+" big.*")
run_in_shell(deltext+" fp.*")
run_in_shell(deltext+" ecp.*")
run_in_shell(deltext+" ecdh.*")
run_in_shell(deltext+" ff.*")
run_in_shell(deltext+" rsa.*")
run_in_shell(deltext+" config_big.h")
run_in_shell(deltext+" config_field.h")
run_in_shell(deltext+" config_curve.h")
run_in_shell(deltext+" config_ff.h")
run_in_shell(deltext+" fp2.*")
run_in_shell(deltext+" fp4.*")
run_in_shell(deltext+" fp12.*")
run_in_shell(deltext+" ecp2.*")
run_in_shell(deltext+" pair.*")
run_in_shell(deltext+" mpin.*")
run_in_shell(deltext+" bls.*")

# create library
run_in_shell("g++ -O3 -c randapi.cpp")
if curve_selected :
	run_in_shell("g++ -O3 -c ecdh_support.cpp")
if rsa_selected :
	run_in_shell("g++ -O3 -c rsa_support.cpp")
if pfcurve_selected :
	run_in_shell("g++ -O3 -c pbc_support.cpp")

run_in_shell("g++ -O3 -c hash.cpp")
run_in_shell("g++ -O3 -c rand.cpp")
run_in_shell("g++ -O3 -c oct.cpp")
run_in_shell("g++ -O3 -c aes.cpp")
run_in_shell("g++ -O3 -c gcm.cpp")
run_in_shell("g++ -O3 -c newhope.cpp")

if sys.platform.startswith("win") :
	run_in_shell("for %i in (*.o) do @echo %~nxi >> f.list")
	run_in_shell("ar rc amcl.a @f.list")
	run_in_shell(deltext+" f.list")

else :
	run_in_shell("ar rc amcl.a *.o")

run_in_shell(deltext+" *.o")


#print("Your section was ")
#for i in range(0,ptr):
#	print (selection[i])

