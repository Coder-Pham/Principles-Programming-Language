.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	invokestatic MCClass/fibonaci(I)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static fibonaci(I)I
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmpne Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifgt Label3
	iload_0
	iconst_0
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
	invokestatic MCClass/fibonaci(I)I
	iload_0
	iconst_2
	isub
	invokestatic MCClass/fibonaci(I)I
	iadd
	ireturn
Label1:
.limit stack 8
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
