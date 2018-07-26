path1 = '/home/cpss/data/KTH/';
path2 = '/home/cpss/data/KTH_idt/';

folderlist = dir(path1);
foldername = {folderlist(:).name};
foldername = setdiff(foldername,{'.','..'});

for i = 1:length(foldername)
    if ~exist([path2,foldername{i}],'dir')
        mkdir([path2,foldername{i}]);
    end
    filelist = dir([path1,foldername{i},'/*.avi']);

    for j = 1:length(filelist)
        videofile = [path1,foldername{i},'/',filelist(j).name];
        outfile = [path2,foldername{i},'/',filelist(j).name(1:end-4),'.gz'];
        videofile = strrep(videofile, '&', '\&'); outfile = strrep(outfile, '&', '\&');
        videofile = strrep(videofile, '(', '\('); outfile = strrep(outfile, '(', '\(');
        videofile = strrep(videofile, ')', '\)'); outfile = strrep(outfile, ')', '\)');
        cmd1 = sprintf('sudo ./release/DenseTrackStab %s | gzip > %s',videofile,outfile);
        system(cmd1);
        cmd2 = sprintf('gunzip %s',outfile);
        system(cmd2);      
    end
end
%system('sudo chmod 777 -R /home/zhong/IDT/hmdb51_idt/');

