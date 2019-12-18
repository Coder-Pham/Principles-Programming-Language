.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	iconst_5
	bipush 13
	invokestatic MCClass/expo(III)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static expo(III)I
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
.var 2 is p I from Label0 to Label1
Label0:
.var 3 is res I from Label0 to Label1
	iconst_1
	istore_3
	iload_0
	iload_2
	irem
	istore_0
Label4:
Label8:
	iload_1
	ifle Label10
	iconst_1
	ifle Label10
Label11:
	iconst_1
	goto Label12
Label10:
	iconst_0
Label12:
	ifgt Label13
	goto Label14
Label13:
Label15:
	iload_3
	iload_0
	imul
	iload_2
	irem
	istore_3
Label16:
Label14:
	iload_1
	iconst_2
	idiv
	istore_1
	iload_0
	iload_0
	imul
	iload_2
	irem
	istore_0
Label9:
Label6:
	iload_1
	iconst_0
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	goto Label4
Label5:
Label7:
	iload_3
	ireturn
Label1:
.limit stack 10
.limit locals 4
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
