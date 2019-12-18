.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static b I
.field static a F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
	sipush 1010
	putstatic MCClass/b I
	getstatic MCClass/b I
	i2f
	fstore_1
	fload_1
	invokestatic io/putFloatLn(F)V
.var 2 is c I from Label0 to Label1
	bipush 12
	getstatic MCClass/b I
	iconst_4
	iadd
	irem
	istore_2
	iload_2
	i2f
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 5
.limit locals 3
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
