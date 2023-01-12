class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        result={}
        for dirs in paths:
            filename_dir=dirs.split()
            dir_name=filename_dir[0]
            for fd in filename_dir[1:]:
                file_and_content=fd.split('(')
                file_name=file_and_content[0]
                content=file_and_content[1][:-1]
                if content not in result:
                    result[content]=[f'{dir_name}/{file_name}']
                else:
                    result[content].append(f'{dir_name}/{file_name}')
        answer=[]
        for _,path in result.items():
            if len(path)>1:
                answer.append(path)
        return answer
                
                    
            