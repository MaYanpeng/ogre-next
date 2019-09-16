#!/usr/bin/env python

texVariableTypeNames =\
[
	"RWTexture1D",
	"RWTexture1DArray",
	"RWTexture2D",
	"RWTexture2DArray",
	"RWTextureCube",
	"RWTextureCubeArray",
	"RWTexture3D",
	"RWTexture2DMS",
	"RWTexture2DMSArray"
]

pixelFormatTypes =\
[
	"unorm float",
	"unorm float2",
	"unorm float3",
	"unorm float4",

	"snorm float",
	"snorm float2",
	"snorm float4",

	"sint",
	"sint2",
	"sint3",
	"sint4",

	"uint",
	"uint2",
	"uint3",
	"uint4",

	"float",
	"float2",
	"float3",
	"float4"
]


file = open( '../../RenderSystems/Direct3D11/include/OgreD3D11PixelFormatToShaderType.inl', 'w+' )

file.write(
'''/// AUTOGENERATED FILE!!! See Scripts/D3D11/GenerateD3D11PixelFormatToShaderType.py
namespace Ogre
{
	static const char c_dataTypes[PixelFormatDataTypes::NumPixelFormatDataTypes*9u][40] =
	{
''' )

for texVariableTypeName in texVariableTypeNames:
	for pixelFormatType in pixelFormatTypes:
		file.write( '		"' + texVariableTypeName + '<' + pixelFormatType + '>",\n' )

file.write( '''	};
}
''' )