.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static fl F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 12
	i2f
	putstatic MCClass/fl F
	ldc 1.2
	fneg
	iconst_3
	i2f
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
Label6:
	getstatic MCClass/fl F
	invokestatic io/putFloatLn(F)V
	return
	bipush 12
	invokestatic io/putInt(I)V
Label7:
Label4:
Label8:
	bipush 43
	invokestatic io/putInt(I)V
	getstatic MCClass/fl F
	bipush 33
	i2f
	fsub
	putstatic MCClass/fl F
	getstatic MCClass/fl F
	invokestatic io/putFloat(F)V
	return
Label9:
Label5:
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
