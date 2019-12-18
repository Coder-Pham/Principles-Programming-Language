.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static check I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	putstatic MCClass/check I
	getstatic MCClass/check I
	iconst_5
	if_icmplt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	goto Label5
Label4:
Label8:
Label14:
	getstatic MCClass/check I
	bipush 20
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label15
	getstatic MCClass/check I
	iconst_1
	isub
	putstatic MCClass/check I
Label16:
	getstatic MCClass/check I
	iconst_2
	iadd
	putstatic MCClass/check I
	goto Label14
Label15:
Label17:
Label10:
	getstatic MCClass/check I
	bipush 10
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label9
	goto Label8
Label9:
Label11:
Label5:
	getstatic MCClass/check I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 13
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
