.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static fl F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 4.0
	iconst_5
	i2f
	fdiv
	bipush 12
	i2f
	fmul
	ldc 34.2
	fdiv
	iconst_3
	i2f
	fsub
	bipush 99
	iconst_4
	idiv
	i2f
	fadd
	iconst_4
	ineg
	ineg
	ineg
	ineg
	ineg
	bipush 7
	imul
	i2f
	fsub
	iconst_3
	ineg
	ineg
	ineg
	ineg
	i2f
	fsub
	bipush 13
	ineg
	ineg
	ineg
	ineg
	i2f
	fsub
	putstatic MCClass/fl F
	getstatic MCClass/fl F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 3
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
