.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I

.method public static assign(II)V
.var 0 is b I from Label0 to Label1
.var 1 is c I from Label0 to Label1
Label0:
	iconst_1
	putstatic MCClass/a I
	iconst_5
	istore_0
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b I from Label0 to Label1
	iconst_1
	istore_1
	getstatic MCClass/a I
	iload_1
	invokestatic MCClass/assign(II)V
	getstatic MCClass/a I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
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
