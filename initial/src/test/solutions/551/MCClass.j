.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I

.method public static cal1()I
Label0:
	getstatic MCClass/a I
	iconst_1
	iadd
	putstatic MCClass/a I
	getstatic MCClass/a I
	ireturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static cal2()F
Label0:
	invokestatic MCClass/cal1()I
	invokestatic MCClass/cal1()I
	imul
	i2f
	freturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static cal3()Z
Label0:
	iconst_1
	ireturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	putstatic MCClass/a I
	invokestatic MCClass/cal3()Z
	invokestatic io/putIntLn(I)V
	invokestatic MCClass/cal2()F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
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
