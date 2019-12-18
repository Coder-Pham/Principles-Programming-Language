.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static isPrime(I)Z
.var 0 is a I from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iload_0
	iconst_2
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	goto Label5
Label4:
	iconst_0
	ireturn
Label5:
	iconst_2
	istore_1
Label8:
	iload_1
	iload_0
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label9
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	goto Label15
Label14:
	iconst_0
	ireturn
Label15:
Label10:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label9:
Label11:
	iconst_1
	ireturn
Label1:
.limit stack 12
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	iconst_1
	istore_1
Label4:
	iload_1
	bipush 10
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	iload_1
	invokestatic MCClass/isPrime(I)Z
	ifgt Label8
	goto Label9
Label8:
	iload_1
	invokestatic io/putIntLn(I)V
Label9:
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 5
.limit locals 2
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
