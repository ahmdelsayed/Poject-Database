USE [ims]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[employee](
    [eid] [int] IDENTITY(1,1) NOT NULL,
    [name] [varchar](100) NULL,
    [email] [varchar](100) NULL,
    [contact] [varchar](100) NULL,
    [gender] [varchar](50) NULL,
    [dob] [varchar](50) NULL,
    [doj] [varchar](50) NULL,
    [pass] [varchar](50) NULL,
    [utype] [varchar](50) NULL,
    [address] [varchar](max) NULL,
    [salary] [varchar](50) NULL,
 CONSTRAINT [PK_employee] PRIMARY KEY CLUSTERED 
(
    [eid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

---------------------------------------------------------------------------------------------------------------------

SET IDENTITY_INSERT [dbo].[employee] ON 
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (1, N'ali', N'practicaldaily80@gmail.com', N'123456789', N'Male', N'11-05-1999', N'08-04-2026', N'12345', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (9, N'ahmed', N'ahmd.elsayedali@gmail.com', N'123456789', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Admin', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (12, N'Ahmed Mohamed', N'ahmedmohamed1@gmail.com', N'1010000001', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (13, N'Mostafa Ali', N'mostafaali2@gmail.com', N'1010000002', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (14, N'Ahmed Mohamed', N'ahmedmohamed3@gmail.com', N'1010000003', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (15, N'Omar Hassan', N'omarhassan4@gmail.com', N'1010000004', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (16, N'Khaled Yassin', N'khaledyassin5@gmail.com', N'1010000005', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (17, N'Khaled Yassin', N'khaledyassin6@gmail.com', N'1010000006', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (18, N'Ahmed Mohamed', N'ahmedmohamed7@gmail.com', N'1010000007', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (19, N'Khaled Yassin', N'khaledyassin8@gmail.com', N'1010000008', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (20, N'Ali Adel', N'aliadel9@gmail.com', N'1010000009', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (21, N'Tamer Fathy', N'tamerfathy10@gmail.com', N'01010000010', N'Male', N'1998-01-01', N'2023-01-01', N'1234', N'Admin', N'Cairo, Egypt', N'3250')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (22, N'Mohamed Samir', N'mohamedsamir11@gmail.com', N'1010000011', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (23, N'Omar Hassan', N'omarhassan12@gmail.com', N'1010000012', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (24, N'Mohamed Samir', N'mohamedsamir13@gmail.com', N'1010000013', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (25, N'Omar Hassan', N'omarhassan14@gmail.com', N'1010000014', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (26, N'Mohamed Samir', N'mohamedsamir15@gmail.com', N'1010000015', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (27, N'Tamer Fathy', N'tamerfathy16@gmail.com', N'1010000016', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (28, N'Mostafa Ali', N'mostafaali17@gmail.com', N'1010000017', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (29, N'Karim Nabil', N'karimnabil18@gmail.com', N'1010000018', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (30, N'Ali Adel', N'aliadel19@gmail.com', N'1010000019', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (31, N'Mostafa Ali', N'mostafaali20@gmail.com', N'01010000020', N'Male', N'1998-01-01', N'2023-01-01', N'1234', N'Admin', N'Cairo, Egypt', N'3500')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (32, N'Karim Nabil', N'karimnabil21@gmail.com', N'1010000021', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (33, N'Ahmed Mohamed', N'ahmedmohamed22@gmail.com', N'1010000022', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (34, N'Hossam Ahmed', N'hossamahmed23@gmail.com', N'1010000023', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (35, N'Karim Nabil', N'karimnabil24@gmail.com', N'1010000024', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (36, N'Ahmed Mohamed', N'ahmedmohamed25@gmail.com', N'1010000025', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (37, N'Tamer Fathy', N'tamerfathy26@gmail.com', N'1010000026', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (38, N'Karim Nabil', N'karimnabil27@gmail.com', N'1010000027', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (39, N'Ali Adel', N'aliadel28@gmail.com', N'1010000028', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (40, N'Omar Hassan', N'omarhassan29@gmail.com', N'1010000029', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (41, N'Tamer Fathy', N'tamerfathy30@gmail.com', N'01010000030', N'Male', N'1998-01-01', N'2023-01-01', N'1234', N'Admin', N'Cairo, Egypt', N'3750')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (42, N'Omar Hassan', N'omarhassan31@gmail.com', N'1010000031', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (43, N'Ali Adel', N'aliadel32@gmail.com', N'1010000032', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (44, N'Tamer Fathy', N'tamerfathy33@gmail.com', N'1010000033', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (45, N'Omar Hassan', N'omarhassan34@gmail.com', N'1010000034', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (46, N'Omar Hassan', N'omarhassan35@gmail.com', N'1010000035', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (47, N'Mostafa Ali', N'mostafaali36@gmail.com', N'1010000036', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (48, N'Omar Hassan', N'omarhassan37@gmail.com', N'1010000037', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (49, N'Hossam Ahmed', N'hossamahmed38@gmail.com', N'1010000038', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (50, N'Tamer Fathy', N'tamerfathy39@gmail.com', N'1010000039', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (51, N'Khaled Yassin', N'khaledyassin40@gmail.com', N'01010000040', N'Male', N'1998-01-01', N'2023-01-01', N'1234', N'Admin', N'Cairo, Egypt', N'4000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (52, N'Khaled Yassin', N'khaledyassin41@gmail.com', N'1010000041', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (53, N'Mostafa Ali', N'mostafaali42@gmail.com', N'1010000042', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (54, N'Mohamed Samir', N'mohamedsamir43@gmail.com', N'1010000043', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (55, N'Ahmed Mohamed', N'ahmedmohamed44@gmail.com', N'1010000044', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (56, N'Karim Nabil', N'karimnabil45@gmail.com', N'1010000045', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (57, N'Ahmed Mohamed', N'ahmedmohamed46@gmail.com', N'1010000046', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (58, N'Karim Nabil', N'karimnabil47@gmail.com', N'1010000047', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (59, N'Mohamed Samir', N'mohamedsamir48@gmail.com', N'1010000048', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (60, N'Khaled Yassin', N'khaledyassin49@gmail.com', N'1010000049', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (61, N'Ahmed Mohamed', N'ahmedmohamed50@gmail.com', N'01010000050', N'Male', N'1998-01-01', N'2023-01-01', N'1234', N'Admin', N'Cairo, Egypt', N'4250')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (62, N'Omar Hassan', N'omarhassan51@gmail.com', N'1010000051', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (63, N'Mostafa Ali', N'mostafaali52@gmail.com', N'1010000052', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (64, N'Youssef Tarek', N'yousseftarek53@gmail.com', N'1010000053', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (65, N'Mohamed Samir', N'mohamedsamir54@gmail.com', N'1010000054', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (66, N'Omar Hassan', N'omarhassan55@gmail.com', N'1010000055', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (67, N'Khaled Yassin', N'khaledyassin56@gmail.com', N'1010000056', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (68, N'Omar Hassan', N'omarhassan57@gmail.com', N'1010000057', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (69, N'Tamer Fathy', N'tamerfathy58@gmail.com', N'1010000058', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (70, N'Khaled Yassin', N'khaledyassin59@gmail.com', N'1010000059', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (71, N'Khaled Yassin', N'khaledyassin60@gmail.com', N'01010000060', N'Male', N'1998-01-01', N'2023-01-01', N'1234', N'Admin', N'Cairo, Egypt', N'4500')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (72, N'Mostafa Ali', N'mostafaali61@gmail.com', N'1010000061', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (73, N'Tamer Fathy', N'tamerfathy62@gmail.com', N'1010000062', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (74, N'Ali Adel', N'aliadel63@gmail.com', N'1010000063', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (75, N'Tamer Fathy', N'tamerfathy64@gmail.com', N'1010000064', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (76, N'Tamer Fathy', N'tamerfathy65@gmail.com', N'1010000065', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (77, N'Mostafa Ali', N'mostafaali66@gmail.com', N'1010000066', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (78, N'Khaled Yassin', N'khaledyassin67@gmail.com', N'1010000067', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (79, N'Karim Nabil', N'karimnabil68@gmail.com', N'1010000068', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (80, N'Khaled Yassin', N'khaledyassin69@gmail.com', N'1010000069', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (81, N'Youssef Tarek', N'yousseftarek70@gmail.com', N'01010000070', N'Male', N'1998-01-01', N'2023-01-01', N'1234', N'Admin', N'Cairo, Egypt', N'4750')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (82, N'Youssef Tarek', N'yousseftarek71@gmail.com', N'1010000071', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (83, N'Mohamed Samir', N'mohamedsamir72@gmail.com', N'1010000072', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (84, N'Ali Adel', N'aliadel73@gmail.com', N'1010000073', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (85, N'Tamer Fathy', N'tamerfathy74@gmail.com', N'1010000074', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (86, N'Hossam Ahmed', N'hossamahmed75@gmail.com', N'1010000075', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (87, N'Hossam Ahmed', N'hossamahmed76@gmail.com', N'1010000076', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (88, N'Ali Adel', N'aliadel77@gmail.com', N'1010000077', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (89, N'Omar Hassan', N'omarhassan78@gmail.com', N'1010000078', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (90, N'Youssef Tarek', N'yousseftarek79@gmail.com', N'1010000079', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (91, N'Ahmed Mohamed', N'ahmedmohamed80@gmail.com', N'01010000080', N'Male', N'1998-01-01', N'2023-01-01', N'1234', N'Admin', N'Cairo, Egypt', N'5000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (92, N'Khaled Yassin', N'khaledyassin81@gmail.com', N'1010000081', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (93, N'Hossam Ahmed', N'hossamahmed82@gmail.com', N'1010000082', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (94, N'Youssef Tarek', N'yousseftarek83@gmail.com', N'1010000083', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (95, N'Karim Nabil', N'karimnabil84@gmail.com', N'1010000084', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (96, N'Youssef Tarek', N'yousseftarek85@gmail.com', N'1010000085', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (97, N'Youssef Tarek', N'yousseftarek86@gmail.com', N'1010000086', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (98, N'Khaled Yassin', N'khaledyassin87@gmail.com', N'1010000087', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (99, N'Mostafa Ali', N'mostafaali88@gmail.com', N'1010000088', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (100, N'Tamer Fathy', N'tamerfathy89@gmail.com', N'1010000089', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (101, N'Omar Hassan', N'omarhassan90@gmail.com', N'01010000090', N'Male', N'1998-01-01', N'2023-01-01', N'1234', N'Admin', N'Cairo, Egypt', N'5250')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (102, N'Karim Nabil', N'karimnabil91@gmail.com', N'1010000091', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (103, N'Tamer Fathy', N'tamerfathy92@gmail.com', N'1010000092', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (104, N'Ahmed Mohamed', N'ahmedmohamed93@gmail.com', N'1010000093', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (105, N'Youssef Tarek', N'yousseftarek94@gmail.com', N'1010000094', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (106, N'Omar Hassan', N'omarhassan95@gmail.com', N'1010000095', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (107, N'Tamer Fathy', N'tamerfathy96@gmail.com', N'1010000096', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (108, N'Tamer Fathy', N'tamerfathy97@gmail.com', N'1010000097', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')

INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (109, N'Hossam Ahmed', N'hossamahmed98@gmail.com', N'1010000098', N'Male', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (110, N'Tamer Fathy', N'tamerfathy99@gmail.com', N'1010000099', N'Female', N'11-05-1999', N'08-04-2026', N'1234', N'Employee', N'Cairo, Egypt', N'15000')
INSERT [dbo].[employee] ([eid], [name], [email], [contact], [gender], [dob], [doj], [pass], [utype], [address], [salary]) VALUES (111, N'Mostafa Ali', N'mostafaali100@gmail.com', N'01010000100', N'Male', N'1998-01-01', N'2023-01-01', N'1234', N'Admin', N'Cairo, Egypt', N'5500')
SET IDENTITY_INSERT [dbo].[employee] OFF
GO

-- =============================================
-- Display all records from the employee table
-- =============================================
SELECT * FROM employee;

-- =============================================
-- Display specific columns
-- =============================================
SELECT name, email, contact, gender, utype, salary 
FROM employee;

-- =============================================
-- Display unique job types (utype)
-- =============================================
SELECT DISTINCT utype FROM employee;

-- =============================================
-- Display unique genders
-- =============================================
SELECT DISTINCT gender FROM employee;

-- =============================================
-- Add a new employee
-- =============================================
SET IDENTITY_INSERT [dbo].[employee] ON;
INSERT INTO employee (eid, name, email, contact, gender, dob, doj, pass, utype, address, salary)
VALUES (112, N'Islam Hassan', N'islam.hassan@gmail.com', N'01123456789', N'Male', N'15-06-2000', N'01-05-2025', N'12345', N'Employee', N'Alexandria, Egypt', N'18000');
SET IDENTITY_INSERT [dbo].[employee] OFF;

-- =============================================
-- Update salary for a specific employee
-- =============================================
UPDATE employee
SET salary = '25000'
WHERE name = 'ali';

-- =============================================
-- Update utype to Admin
-- =============================================
UPDATE employee
SET utype = 'Admin'
WHERE name = 'Ahmed Mohamed';

-- =============================================
-- Delete an employee by eid
-- =============================================
DELETE FROM employee 
WHERE eid = 2;

-- =============================================
-- Basic Filters
-- =============================================
SELECT * FROM employee WHERE utype = 'Admin';
SELECT * FROM employee WHERE gender = 'Male';
SELECT * FROM employee WHERE name LIKE 'Ahmed%';
SELECT * FROM employee WHERE CAST(salary AS INT) > 15000;

-- =============================================
-- Aggregate Functions
-- =============================================
SELECT COUNT(*) AS Total_Employees FROM employee;

SELECT utype, COUNT(*) AS Count FROM employee GROUP BY utype;
SELECT gender, COUNT(*) AS Count FROM employee GROUP BY gender;

SELECT AVG(CAST(salary AS INT)) AS Average_Salary FROM employee;

SELECT 
    MAX(CAST(salary AS INT)) AS Highest_Salary,
    MIN(CAST(salary AS INT)) AS Lowest_Salary
FROM employee;

-- =============================================
-- Advanced Queries (New Additions)
-- =============================================

-- Count employees per utype with more than 10 employees (HAVING)
SELECT utype, COUNT(*) AS Employee_Count
FROM employee
GROUP BY utype
HAVING COUNT(*) > 10;

-- Employees earning above average salary (Subquery)
SELECT name, utype, salary
FROM employee
WHERE CAST(salary AS INT) > (SELECT AVG(CAST(salary AS INT)) FROM employee);

-- Employees with salary higher than all Admins
SELECT name, salary, utype
FROM employee
WHERE CAST(salary AS INT) > ALL (SELECT CAST(salary AS INT) FROM employee WHERE utype = 'Admin');

-- Number of employees hired per year
SELECT 
    YEAR(doj) AS Join_Year,
    COUNT(*) AS Employee_Count
FROM employee
GROUP BY YEAR(doj)
ORDER BY Join_Year DESC;

-- Ranking employees by salary (Highest to Lowest)
SELECT 
    name,
    utype,
    salary,
    ROW_NUMBER() OVER (ORDER BY CAST(salary AS INT) DESC) AS Salary_Rank
FROM employee;

-- Top 5 highest paid employees
SELECT TOP 5 name, utype, salary
FROM employee
ORDER BY CAST(salary AS INT) DESC;

-- Employees classified by salary level
SELECT 
    name,
    utype,
    salary,
    CASE 
        WHEN CAST(salary AS INT) >= 20000 THEN 'Senior'
        WHEN CAST(salary AS INT) BETWEEN 10000 AND 19999 THEN 'Mid Level'
        ELSE 'Junior'
    END AS employee_level
FROM employee;

-- Count of duplicate names
SELECT name, COUNT(*) AS Duplicate_Count
FROM employee
GROUP BY name
HAVING COUNT(*) > 1;

-- Admins with high salary
SELECT name, email, salary 
FROM employee 
WHERE utype = 'Admin' AND CAST(salary AS INT) >= 4000;

-- Female employees who are Admin
SELECT * FROM employee 
WHERE gender = 'Female' AND utype = 'Admin';

-- Search employees in Cairo
SELECT * FROM employee 
WHERE address LIKE '%Cairo%';

-- List all Admin emails
SELECT name, email, salary 
FROM employee 
WHERE utype = 'Admin'
ORDER BY CAST(salary AS INT) DESC;

-- Employees who joined in 2023 or later
SELECT * FROM employee 
WHERE doj >= '2023-01-01';