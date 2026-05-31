#!/usr/bin/env -S dotnet fsi
#r "nuget: FSharpMyExt, 2.0.0-prerelease.11"
#load @"TimecodeMediaSplitter/src/ffmpegApi.fsx"
open FfmpegApi
open FsharpMyExtension.Containers
open FsharpMyExtension.Serialization.Serializers
open FsharpMyExtension.IO
open System.IO

module Result =
    let ofOption err = function
        | None -> Error err
        | Some x -> Ok x

type ProcResult = int * string * string

module ProcResult =
    let toResult ((code, stdOut, stdErr): ProcResult) =
        if code = 0 then
            Ok stdErr // хрен знает почему. но ffmpeg фигачит всё в err
        else
            Error (code, stdOut, stdErr)

[<RequireQualifiedAccess>]
type MaxVolumeError =
    | Ffmpeg of ProcResult
    | MaxVolumeNotFound

let maxVolume input =
    FfMpeg.startProc
        (String.concat " " [
            $"-i \"%s{input}\""
            "-af \"volumedetect\" -vn -sn -dn -f null -"
        ])
    |> ProcResult.toResult
    |> Result.mapError MaxVolumeError.Ffmpeg
    |> Result.bind (fun stdOut ->
        Regex.matchOther """max_volume: (-\d+.\d+) dB""" stdOut
        |> Result.ofOption MaxVolumeError.MaxVolumeNotFound
        |> Result.map (Seq.head >> float)
    )

let louder volume outputDir (inputFile: string) =
    let dest =
        Path.Combine (outputDir, (Path.GetFileName inputFile))
    FfMpeg.startProc
        (String.concat " " [
            "-y"
            $"-i \"%s{inputFile}\""
            $"-af volume=%s{volume}"
            $"\"%s{dest}\""
        ])

let louders pattern outputDir inputDir =
    Directory.EnumerateFiles(inputDir, pattern)
    |> Seq.iter (fun inputFile ->
        maxVolume inputFile
        |> Result.iter (fun maxVolume ->
            let result =
                louder $"%g{abs maxVolume}dB" outputDir inputFile
            ()
        )
        ()
    )

louders "p-*.mp3" "output" "src/game/voices"
louders "w-*.mp3" "output" "src/game/voices"
