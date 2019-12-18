.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
.var 2 is y I from Label0 to Label1
	bipush 10
	istore_1
	bipush 100
	istore_2
.var 3 is a F from Label0 to Label1
.var 4 is b F from Label0 to Label1
.var 5 is c F from Label0 to Label1
	iload_1
	i2f
	ldc 25.4
	fdiv
	fstore_3
	iload_2
	i2f
	ldc 12.4
	fdiv
	fstore 4
	fload_3
	fload 4
	fmul
	iload_1
	i2f
	fadd
	iload_2
	i2f
	fdiv
	iload_2
	i2f
	fload_3
	fload 4
	fmul
	iconst_2
	iload_1
	idiv
	i2f
	fadd
	fdiv
	fadd
	fstore 5
	fload 5
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 9
.limit locals 6
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
