.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is n1 I from Label0 to Label1
.var 3 is n2 I from Label0 to Label1
.var 4 is next I from Label0 to Label1
	iconst_0
	istore 4
	iload 4
	istore_2
	iload_2
	iconst_1
	iadd
	istore_3
	iconst_1
	istore_1
Label4:
	iload_1
	bipush 25
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
Label8:
	iload_1
	iconst_1
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	goto Label13
Label12:
Label14:
	ldc "first:"
	invokestatic io/putString(Ljava/lang/String;)V
	iload_2
	invokestatic io/putIntLn(I)V
	goto Label6
Label15:
Label13:
	iload_1
	iconst_2
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifgt Label18
	goto Label19
Label18:
Label20:
	ldc "second:"
	invokestatic io/putString(Ljava/lang/String;)V
	iload_3
	invokestatic io/putIntLn(I)V
	goto Label6
Label21:
Label19:
	iload_2
	iload_3
	iadd
	istore 4
	iload_3
	istore_2
	iload 4
	istore_3
	iload 4
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
	return
Label1:
	return
.limit stack 13
.limit locals 5
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
