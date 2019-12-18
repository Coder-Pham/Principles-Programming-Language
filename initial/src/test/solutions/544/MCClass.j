.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static fl F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is fl F from Label0 to Label1
.var 2 is i I from Label0 to Label1
	iconst_1
	istore_2
	iload_2
	ineg
	i2f
	fstore_1
	fload_1
	invokestatic io/putFloatLn(F)V
.var 3 is a I from Label0 to Label1
	bipush 12
	iload_2
	iconst_4
	iadd
	irem
	istore_3
	iload_3
	i2f
	invokestatic io/putFloat(F)V
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
