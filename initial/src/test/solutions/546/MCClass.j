.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b I from Label0 to Label1
Label2:
	iconst_4
	istore_1
.var 2 is a I from Label2 to Label3
Label4:
	iconst_5
	istore_2
.var 3 is i I from Label4 to Label5
	iconst_3
	istore_3
	iload_1
	iload_2
	isub
	iload_3
	isub
	i2f
	invokestatic io/putFloatLn(F)V
	iconst_5
	istore_1
Label5:
	iload_1
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 5
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
