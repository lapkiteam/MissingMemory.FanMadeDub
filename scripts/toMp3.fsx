#!/usr/bin/env -S dotnet fsi
#r "nuget: FSharpMyExt, 2.0.0-prerelease.11"
#load @"TimecodeMediaSplitter/src/ffmpegApi.fsx"
open FfmpegApi
open FsharpMyExtension.IO
open System.IO

let filesToMp3 dir =
    Directory.EnumerateFiles(dir)
    |> Seq.iter (fun src ->
        let dest =
            Path.changeExt ".mp3" src
        let options: FfMpeg.Options = {
            OverwriteOutput = true
            Start = None
            End = None
            Metadata = None
            CopyAudio = false
            CopyVideo = false
            ASync = false
        }
        let _ = FfMpeg.start src options dest
        ()
    )

match fsi.CommandLineArgs[1..] with
| [|dir|] ->
    filesToMp3 dir
| xs ->
    printfn "error!"
