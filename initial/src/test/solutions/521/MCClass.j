.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static cal(I)I
.var 0 is a I from Label0 to Label1
Label0:
Label2:
	iload_0
	bipush 10
	ineg
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
Label10:
	iload_0
	iconst_2
	ineg
	iadd
	istore_0
	goto Label4
Label11:
	goto Label9
Label8:
	goto Label5
Label9:
Label4:
	iconst_1
	ifle Label3
	goto Label2
Label3:
Label5:
	iload_0
	ireturn
Label1:
.limit stack 6
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	iconst_1
	istore_1
	iload_1
	invokestatic MCClass/cal(I)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
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
