def getDict():
	""" Use this function to get a dictionary from SVM classification to the Math symbol recognized """
	d = {}
	d[0] = 0
	d[1] = 1
	d[2] = 2
	d[3] = 3
	d[4] = 4
	d[5] = 5
	d[6] = 6
	d[7] = 7
	d[8] = 8
	d[9] = 9
	d[10] = '-'
	#d[11] = '!'
	d[12] = '('
	d[13] = ')'
	#d[14] = ','
	#d[15] = '['
	#d[16] = ']'
	#d[17] = '{'
	#d[18] = '}'
	d[19] = '+'
	#d[20] = 'dot'
	#d[20] = '='
	d[21] = 'A'
	d[22] = 'alpha'
	#d[23] = 'ascii_124'
	d[24] = 'b'
#	d[25] = 'beta'
	d[26] = 'C'
	#d[27] = 'cos'
	d[28] = 'd'
	d[29] = 'Delta'
	#d[30] = 'division'
	d[31] = 'e'
	#d[32] = 'exists'
	d[33] = 'f'
#	d[34] = 'forall'
	d[35] = 'forward_slash'
	d[36] = 'G'
#	d[37] = 'gamma'
	#d[38] = '>='
	d[39] = 'gt'
	d[40] = 'H'
	#d[41] = 'i'
	#d[42] = 'in'
	d[43] = 'infty'
	d[44] = 'int'
	#d[45] = 'j'
	d[46] = 'k'
	d[47] = 'l'
	#d[48] = 'lambda'
	#d[49] = 'ldots'
	#d[50] = '<='
	#d[51] = 'limit'
	#d[52] = 'log'
	d[53] = 'lt'
	d[54] = 'M'
	#d[55] = 'mu'
	d[56] = 'N'
	d[57] = 'neq'
	d[58] = 'o'
	d[59] = 'p'
	#d[60] = 'phi'
	d[61] = 'pi'
	#d[62] = 'plus-minus'
	#d[63] = 'prime'
	d[64] = 'q'
	d[65] = 'R'
	#d[66] = 'rightarrow'
	d[67] = 'S'
	d[68] = 'sigma'
	#d[69] = 'sin'
	d[70] = 'sqrt'
	d[71] = 'sum'
	d[72] = 'T'
	#d[73] = 'tan'
	d[74] = 'theta'
	#d[75] = 'times'
	d[76] = 'u'
	d[77] = 'v'
	d[78] = 'w'
	d[79] = 'X'
	d[80] = 'y'
	d[81] = 'z'

	return d

def getAccuracies():
	d = {}
	d[0] = 0.7846
	d[1] = 0.7355
	d[2] = 0.8056
	d[3] = 0.7707
	d[4] = 0.7846
	return d