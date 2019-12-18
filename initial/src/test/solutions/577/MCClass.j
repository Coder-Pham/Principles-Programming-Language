.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I

.method public static fact(I)I
.var 0 is x I from Label0 to Label1
Label0:
.var 1 is fact I from Label0 to Label1
.var 2 is i I from Label0 to Label1
	iconst_1
	istore_1
	iconst_1
	istore_2
Label4:
	iload_2
	iload_0
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
Label8:
	iload_1
	iload_2
	imul
	istore_1
Label9:
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label5:
Label7:
	iload_1
	ireturn
Label1:
.limit stack 7
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	putstatic MCClass/a I
Label4:
	getstatic MCClass/a I
	bipush 15
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
Label8:
	getstatic MCClass/a I
	invokestatic MCClass/fact(I)I
	invokestatic io/putIntLn(I)V
Label9:
Label6:
	getstatic MCClass/a I
	iconst_1
	iadd
	putstatic MCClass/a I
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 5
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
