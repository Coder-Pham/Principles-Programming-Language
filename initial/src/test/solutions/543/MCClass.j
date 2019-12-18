.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static fl F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 13.5
	fneg
	fneg
	fneg
	fneg
	putstatic MCClass/fl F
	getstatic MCClass/fl F
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
