.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static binomialCoeff(II)I
.var 0 is n I from Label0 to Label1
.var 1 is k I from Label0 to Label1
Label0:
	iload_1
	iconst_0
	if_icmpne Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifgt Label3
	iload_1
	iload_0
	if_icmpne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label2
Label3:
	iconst_1
	goto Label4
Label2:
	iconst_0
Label4:
	ifgt Label9
	goto Label10
Label9:
	iconst_1
	ireturn
Label10:
	iload_0
	iconst_1
	isub
	iload_1
	iconst_1
	isub
	invokestatic MCClass/binomialCoeff(II)I
	iload_0
	iconst_1
	isub
	iload_1
	invokestatic MCClass/binomialCoeff(II)I
	iadd
	ireturn
Label1:
.limit stack 8
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "n = 5, k = 2 => 5C2 = "
	invokestatic io/putString(Ljava/lang/String;)V
	iconst_5
	iconst_2
	invokestatic MCClass/binomialCoeff(II)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
