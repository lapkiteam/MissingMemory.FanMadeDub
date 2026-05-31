#!/usr/bin/env -S dotnet fsi
#r "nuget: FSharpMyExt, 2.0.0-prerelease.11"
#load @"TimecodeMediaSplitter/src/ffmpegApi.fsx"
open FfmpegApi
open FsharpMyExtension.IO
open System.IO

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

let louders pattern volume outputDir inputDir =
    Directory.EnumerateFiles(inputDir, pattern)
    |> Seq.iter (fun inputFile ->
        let result =
            louder volume outputDir inputFile
        ()
    )

louders "p-*.mp3" "8.055dB" "output" "src/game/voices"
louders "w-*.mp3" "14.065dB" "output" "src/game/voices"
// louders "p-*.mp3" 3.5 "output" "src/game/voices"
// louders "w-*.mp3" 5.0 "output" "src/game/voices"
