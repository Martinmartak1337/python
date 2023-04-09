def main():
	#no =0
	#abcdef = 0
	alphabet = ['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','Q','S','T','U','V','W','X','Y','Z']
	ciphertext = "BT JPX RMLX PCUV AMLX ICVJP IBTWXR CI M LMT'R PMTN, MTN YVCJX CDXV MWMBTRJ JPX AMTNGXRJBAH UQCT JPX QGMRJXV CI JPX YMGG CI JPX HBTW'R QMGMAX; MTN JPX HBTW RMY JPX QMVJ CI JPX PMTN JPMJ YVCJX. JPXT JPX HBTW'R ACUTJXTMTAX YMR APMTWXN,MTN PBR JPCUWPJR JVCUFGXN PBL, RC JPMJ JPX SCBTJR CI PBR GCBTR YXVX GCCRXN, MTN PBR HTXXR RLCJX CTX MWMBTRJ MTCJPXV. JPX HBTW AVBXN MGCUN JC FVBTW BT JPX MRJVCGCWXVR, MPS APMGNXMTR, MTN JPX RCCJPRMEXVR. MTN JPX HBTW RQMHX, MTN RMBN JC JPX YBRX LXT CI FMFEGCT, YPCRCXDXV RPMGG VXMN JPBR YVBJBTW, MTN RPCY LX JPX BTJXVQVXJMJBCT JPXVXCI, RPMGG FX AGCJPXN YBJP RAMVGXJ, MTN PMDX M APMBT CI WCGN MFCUJ PBR TXAH, MTN RPMGG FX JPX JPBVN VUGXV BT JPX HBTWNCL. JPXT AMLX BT MGG JPX HBTW'R YBRX LXT; FUJ JPXE ACUGN TCJ VXMN JPX YVBJBTW, TCV LMHX HTCYT JC JPX HBTW JPX BTJXVQVXJMJBCT JPXVXCI. JPXT YMR HBTW FXGRPMOOMV WVXMJGE JVCUFGXN, MTN PBR ACUTJXTMTAX YMR APMTWXN BT PBL, MTN PBR GCVNR YXVX MRJCTBRPXN. TCY JPX KUXXT, FE VXMRCT CI JPX YCVNR CI JPX HBTW MTN PBR GCVNR, AMLX BTJC JPX FMTKUXJ PCURX; MTN JPX KUXXT RQMHX MTN RMBN, C HBTW, GBDX ICVXDXV; GXJ TCJ JPE TPCUWPJR JVCUFGX JPXX, TCV GXJ JPE ACUTJXTMTAX FX APMTWXN; JPXVX BR M LMT BT JPE HBTWNCL, BT YPCL BR JPX RQBVBJ CI JPX PCGE WCNR; MTN BT JPX NMER CI JPE IMJPXV GBWPJ MTN UTNXVRJMTNBTW MTN YBRNCL, GBHX JPX YBRNCL CI JPX WCNR, YMR ICUTN BT PBL; YPCL JPX HBTW TXFUAPMNTXOOMV JPE IMJPXV, JPX HBTW, B RME, JPE IMJPXV, LMNX LMRJXV CI JPX LMWBABMTR, MRJVCGCWXVR, APMGNXMTR, MTN RCCJPRMEXVR; ICVMRLUAP MR MT XZAXGGXTJ RQBVBJ, MTN HTCYGXNWK, MTN UTNXVRJMTNBTW, BTJXVQVXJBTW CI NVXMLR, MTN RPCYBTW CI PMVN RXTJXTAXR, MTN NBRRCGDBTW CI NCUFJR, YXVX ICUTN BT JPX RMLX NMTBXG YPCL JPX HBTW TMLXN FXGJXRPMOOMV; TCY GXJ NMTBXG FX AMGGXN, MTN PX YBGG RPCY JPX BTJXVQVXJMJBCT. JPX IBVRJ ACNXYCVN BR CJPXGGC"
	new_ciphertext = [char for char in ciphertext]
	abs = [None] * len(ciphertext)
	bam = ['E', 'N', 'T', 'A', 'H', 'O', 'S', 'I', 'D', 'R', 'L', 'G', 'W', 'C', 'M', 'F', 'U', 'K', 'B', 'Y', 'P',
       'V', 'Z', 'Q', 'J', 'X']
	new_list = [0] * len(alphabet)
	output = [None] * len(ciphertext)
	for i in range(0, len(ciphertext)-1):
		for j in range(0, len(alphabet)-1):
			if(new_ciphertext[i] == alphabet[j]):
				new_list[j] +=1
	print(alphabet)		
	while(True):
		ihatefunctiondefinitions = sorted(new_list)
		if(ihatefunctiondefinitions == new_list):
			break
		#abcdef+=1
		for k in range(0, len(alphabet)-1):
			if(k+1 <= len(alphabet)-1):
				if(new_list[k] > new_list[k+1]):
					#no+=1
					xyz = new_list[k+1]
					abc = alphabet[k+1]
					new_list[k+1] = new_list[k]
					alphabet[k+1] = alphabet[k]
					new_list[k] = xyz
					alphabet[k] = abc
				
	for l in range(0, len(ciphertext)-1):
		for b in range(len(alphabet)-1):
			if(ciphertext[l] == alphabet[len(alphabet)-1-b]): 
				output[l] = bam[b]

	print(alphabet)
	print(new_list)
	#print(bam)
	print(output)	

main()				